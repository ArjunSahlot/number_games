#!/bin/bash

download_link=https://github.com/ArjunSahlot/number_games/archive/master.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir master.zip \
&& rm -rf master.zip \
&& mv $temporary_dir/number_games-master $1/number_games \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/number_games[0m"
