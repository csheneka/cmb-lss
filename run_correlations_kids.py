import argparse

from utils import get_config, save_correlations
from experiment import Experiment

# Read input arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', dest='config_name', required=True, help='configuration name')
parser.add_argument('-t', '--tag', dest='tag', help='tag, added as suffix to the experiment name')
args = parser.parse_args()

# Read YAML configuration file
config = get_config(args.config_name)
config.experiment_tag = args.tag
config.read_data_correlations_flag = False
config.read_covariance_flag = False
config.redshifts_to_fit = []
config.fit_bias_to_tomo = False
print(config.__dict__)

# Iterate through parameters
for r_max in [21, 22, 23, 23.5]:
    for qso_min_proba in [0.9, 0.98, 0.998, 0.999]:
        print('Processing: r_max={}, qso_min_proba={}'.format(r_max, qso_min_proba))
        config.r_max = r_max
        config.qso_min_proba = qso_min_proba

        experiment = Experiment(config, set_data=True, set_maps=True)
        experiment.set_correlations()
        save_correlations(experiment)
