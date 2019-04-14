# -*- coding: utf-8 -*-
from urllib import request
from .config import RELEASES_URLS
import os
import sys
import zipfile
import glob


def get_release_dir(release):

    return os.path.join(default_download_dir(), release)


def get_release_datasets_dir(release):

    release_dir = get_release_dir(release)

    for dataset_dirpath in glob.iglob(os.path.join(release_dir, '*/')):

        dataset_name = os.path.basename(os.path.normpath(dataset_dirpath))

        yield dataset_name


def get_dataset_files(release, dataset):

    release_dir = get_release_dir(release)
    dataset_dir = os.path.join(release_dir, dataset)

    return glob.glob(os.path.join(dataset_dir, '**/*.xml'), recursive=True)


# from https://github.com/nltk/nltk/blob/develop/nltk/downloader.py
def default_download_dir():

    if sys.platform == 'win32' and 'APPDATA' in os.environ:
        homedir = os.environ['APPDATA']

    else:
        homedir = os.path.expanduser('~/')
        if homedir == '~/':
            raise ValueError("Could not find a default download directory")

    download_dir = os.path.join(homedir, 'webnlg_data')

    if not os.path.isdir(download_dir):
        os.mkdir(download_dir)

    return download_dir


def download(release, force=False):

    if release not in RELEASES_URLS:
        raise ValueError(f'{release} is not an available release name.'
                         'Available releases are {RELEASES.keys()}')

    release_dir = get_release_dir(release)

    if os.path.isdir(release_dir):

        if force:
            os.rmdir(release_dir)
        else:
            raise ValueError(f'{release} is already dowloaded at {release_dir}')

    temp_zip_filepath = os.path.join(default_download_dir(), 'temp')

    request.urlretrieve(RELEASES_URLS[release], temp_zip_filepath)

    with zipfile.ZipFile(temp_zip_filepath, 'r') as zip_ref:

        zip_ref.extractall(default_download_dir())

    os.remove(temp_zip_filepath)
