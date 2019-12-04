#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the ``django-user-tasks`` admin module.
"""

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AdminTestCase(TestCase):
    """
    Tests for the ``user_tasks`` application's Django admin pages.
    """
    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='password',
            is_staff=True,
            is_superuser=True,
        )
        self.client.login(username=self.user.username, password='password')

    def test_artifact_list(self):
        """
        Make sure the main UserTaskArtifact admin page loads.
        """
        response = self.client.get(reverse('admin:user_tasks_usertaskartifact_changelist'))
        assert response.status_code == 200

    def test_status_list(self):
        """
        Make sure the main UserTaskStatus admin page loads.
        """
        response = self.client.get(reverse('admin:user_tasks_usertaskstatus_changelist'))
        assert response.status_code == 200
