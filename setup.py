# ----------------------------------------------------------------------------
# Copyright (c) 2022-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

setup(
    name='q2-moshpit',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD-3-Clause',
    packages=find_packages(),
    author="Michal Ziemski",
    author_email="ziemski.michal@gmail.com",
    description="QIIME 2 plugin for metagenome analysis.",
    url="https://github.com/bokulich-lab/q2-moshpit",
    entry_points={
        'qiime2.plugins':
        ['q2-moshpit=q2_moshpit.plugin_setup:plugin']
    },
    package_data={
        'q2_moshpit': ['citations.bib'],
        'q2_moshpit.metabat2.tests': [
            'data/*', 'data/bins/samp1/*', 'data/contigs/*',
            'data/depth/*', 'data/maps/*'
        ],
        'q2_moshpit.kraken2.tests': [
            'data/*', 'data/mags/*', 'data/mags/*/*',
            'data/single-end/*', 'data/paired-end/*',
            'data/db/*', 'data/reports-mags/*',
            'data/reports-mags/*/*', 'data/outputs-mags/*',
            'data/outputs-mags/*/*', 'data/seqs/*'
        ]
    },
    zip_safe=False,
)
