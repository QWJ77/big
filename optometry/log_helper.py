import logging
import logzero

# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
logzero.logfile("rotating-logfile.log", maxBytes=1024*1024, backupCount=3)
logzero.loglevel(logging.DEBUG)

# Set a custom formatter
formatter = logging.Formatter('%(asctime)s %(levelname)-s %(message)s', "%Y-%m-%d %H:%M:%S")
logzero.formatter(formatter)
