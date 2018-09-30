import pytest
from test_tube.hpc import SlurmCluster
from test_tube.argparse_hopt import HyperOptArgumentParser


def test_slurm_time_to_seconds():
    parser = HyperOptArgumentParser()
    parsed = parser.parse_args()
    cluster = SlurmCluster('/home/travis', parsed)

    assert cluster.slurm_time_to_seconds('15:00') == 900
    assert cluster.slurm_time_to_seconds('1-12:20:12') == 130812
    assert cluster.slurm_time_to_seconds('1:20:12') == 4812
    assert cluster.slurm_time_to_seconds('00:20:12') == 1212
    assert cluster.slurm_time_to_seconds('00:00:12') == 12
    assert cluster.slurm_time_to_seconds('12') == 12


if __name__ == '__main__':
    pytest.main([__file__])
