# This container defines a base embarcadero mind machine image.
FROM jfloff/alpine-python:recent-onbuild

RUN git clone -b prereleases/v23 https://github.com/rainbow-mind-machine/embarcadero-mind-machine.git emm
RUN cd /emm && \
    /usr/bin/env pip install -r requirements.txt && \
    /usr/bin/env python /emm/setup.py build && \
    /usr/bin/env python /emm/setup.py install
