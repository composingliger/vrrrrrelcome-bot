.PHONY: help install

PREFIX := /usr/local

help:
	@echo 'Run `make install` to install'

install:
	install -D -t $(PREFIX)/bin vrrrrrelcome-bot
	install -D -t $(PREFIX)/lib/systemd/system systemd/vrrrrrelcome-bot.service
	install -D -t $(PREFIX)/share/vrrrrrelcome-bot/data data/welcome.ogg
