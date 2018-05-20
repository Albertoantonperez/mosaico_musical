import os
import io
import random
import pickle
import pdb
import sys
import getopt

# Initializing random seed
random.seed(1234)

def list_splitting(user_list, test_pct):
    """ Function that returns random train and test sets for a given user.
    
        Args:
          user_list: list of data to be split.
          test_pct: percentage of elements that go to the test set.
    
        Returns:
          Two random lists with the proportional percentage of train and test.
    """
    test_elements = int(round(test_pct * len(user_list)))
    # Randomly shuffling a copy of the original list
    shuffled = user_list
    random.shuffle(shuffled)
    return shuffled[test_elements:], shuffled[:test_elements]
    
def write_sets(train, test):
    """ Function that writes to the train and test pickle files.
    
        Args:
          train: list with train data to be written.
          test: list with test data to be written.
    
        Returns:
          Two random lists with the proportional percentage of train and test.
    """
    pickle.dump(train, train_file)
    pickle.dump(test, test_file)

def show_help():
    print ("""
    {script} is a script to create random sets of users' listenings. 
    It is possible to specify the percentage of data for the sets and 
    the number of users that they will have.
    
    Usage: {script} [options]
    
    Options:
        -t, --test=:  specifies the percentage of the data that will be in the test set. 
                      The rest will be in the trainig. Value from 0 to 1. 
                      If not set, 0.2 (20%) will be used.
        -u, --users=: number of users that will be in each set. If not set, all wil be used.
        -h :          displays this help
        
    Examples:
        {script} -t 0.25
        {script} --users=1000 
        {script} -t 0.3 -u 1000
    """.format(script = os.path.basename(__file__)))
 
def check_params(argv):
    """ Function that reads command line parameters and stablishes default and custom
        values for the execution of the program.

        Args:
            argv: command line parameters.

        Returns:
            test_pct: percentage of the data that will be in the test set. The rest will be in the trainig.
                      Value from 0 to 1
            max_users: number of users that will be in each set.
    """

    # Default values
    test_pct = 0.2
    max_users = 10000000000  # All by default
    
    if len(argv) > 1:
        try:
            opts, args = getopt.getopt(argv[1:],"ht:u:",["test=", "users="])
        except getopt.GetoptError as err:
            print (str(err))
            show_help()
            sys.exit(2)
        for opt, arg in opts:
            # Help
            if opt == '-h':
                show_help()
                sys.exit(0)
            # Test
            elif opt in ("-t", "--test"):
                if 0 <= float(arg) <= 1:
                    test_pct = float(arg)
                else:
                    print ("WARNING: incorrect test percentage. Value must be between 0 and 1. Using {0} by default".format(max_users))
            # Users
            elif opt in ("-u", "--users"):
                if 0 < int(arg):
                    max_users = int(arg)
                else:
                    print ("ERROR: incorrect number of users. It must be greater then 0. Leave blank for all the users.")
                    sys.exit(1)
    return test_pct, max_users

if __name__ == '__main__':
    # Get parameters
    test_pct, max_users = check_params(sys.argv)

    # Open the output files
    train_file_path = "data/train_listenings.pkl"
    test_file_path = "data/test_listenings.pkl"
    listenings_file = "data/train_triplets_sorted.txt"

    # pdb.set_trace()
    # Delete the files if they already exist
    try:
        os.remove(train_file_path)
        os.remove(test_file_path)
    except OSError:
        pass

    # Open them. We'll be writting as we read
    test_file = open(test_file_path, 'ab')
    train_file = open(train_file_path, 'ab')

    # Initializing variables
    last_user = ""
    user_count = 0
    user_data = []

    # Read the ordered user data line by line
    with io.open(listenings_file, 'r') as f:
        for line in f: #.readlines():
            # Read a user and then distribute it between sets
            record = line.split()
            user = record[0]
            # The first time we do nothing
            if last_user == "":
                last_user = user
            if user != last_user:
                # pdb.set_trace()
                # Change of user. Save it in train and test
                write_sets(*list_splitting(user_data, test_pct))
                last_user = user
                user_count += 1
                user_data = []
            else:
                # Add line to user_data
                user_data.append(record)
            if user_count == max_users:
                # Close all files and exit
                test_file.close()
                train_file.close()
                f.close()
                sys.exit()
# If we finish reading the file, we add the last user and close the ouput files
user_train_data, user_test_data = list_splitting(user_data, test_pct)
write_sets(user_train_data, user_test_data)
test_file.close()                
train_file.close()             