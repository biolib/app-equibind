FROM nvidia/cuda:10.2-runtime-ubuntu18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      wget \
      unzip \
      && rm -rf /var/lib/apt/lists/*

RUN wget -q -P /tmp \
  https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \
    && rm /tmp/Miniconda3-latest-Linux-x86_64.sh

COPY equibind/environment.yml .
ENV PATH="/opt/conda/bin:$PATH"
RUN conda env create -f environment.yml
COPY equibind/ .
RUN chmod +x run.sh
RUN mkdir -p /data/results/trajectories
#ENTRYPOINT ["/run.sh"]
