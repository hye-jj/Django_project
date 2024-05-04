from django.test import TestCase

# Create your tests here.
# 테스트 코드 추가
# 실패하는 코드
class TestView(TestCase):
    def test_post_list(self):
        self.assertEquals(2,3)