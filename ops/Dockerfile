FROM ruby:3.2-slim AS base

RUN	apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends ruby-full build-essential zlib1g-dev

RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc

RUN gem -v
RUN gem install jekyll bundler

# Set the working directory
WORKDIR /app
