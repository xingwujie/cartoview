from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from geonode.people.models import Profile


class CartoviewAppsViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/apps/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('app_manager_base_url'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('app_manager_base_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'app_manager/apps.html')
        self.assertTrue("apps" in resp.context)


class CartoviewManageAppsViewTest(TestCase):
    fixtures = ['sample_admin.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.username = "staff_user"
        self.password = "staff_user"
        self.email = "staff_user@staff_user.com"
        self.user = Profile.objects.create_superuser(
            self.username, self.email, self.password)
        self.client.login(username=self.username, password=self.password)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/apps/manage/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("manage_apps"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('manage_apps'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'app_manager/manage.html')
        self.assertTrue("apps" in resp.context)
        self.assertTrue("site_apps" in resp.context)
        self.assertTrue("version_info" in resp.context)
