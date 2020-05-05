#!/bin/bash

pip3 install pytest pytest-cov pylint mock
pytest tests --doctest-modules --junitxml=test-results/unit/test-results.xml --cov=. --cov-report=xml:test-results/coverage.xml --cov-report=html:test-results/htmlcov
