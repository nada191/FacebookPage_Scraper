import unittest


class MyTestCase(unittest.TestCase):
    def test_get_posts_fields_presence(self):
        """ Check if all fields are present """
        posts = self.scrape_data()
        for post in posts:
            self.assertIn('shares', post)
            self.assertIn('reaction_count', post)
            self.assertIn('comments', post)
            self.assertIn('content', post)
            self.assertIn('posted_on', post)
            self.assertIn('video', post)
            self.assertIn('image', post)

    def test_get_posts(self): # page_name = mosaiquefm
        """ Check if the scraped data is as expected """
        expected_result = {'shares': '0', 'reaction_count': '48', 'comments': '6', 'content': 'التقدّم في إعداد المخطّط التنموي 2023-2025\n', 'posted_on': '15 mins', 'video': None, 'image': ['https://external.ftun1-2.fna.fbcdn.net/emg1/v/t13/14398705836475522597?url=https%3A%2F%2Fcontent.mosaiquefm.net%2Fuploads%2Fcontent%2Fthumbnails%2F1659630831_media.jpg&fb_obo=1&utld=mosaiquefm.net&stp=c0.5000x0.5000f_dst-jpg_flffffff_p500x261_q75&ccb=13-1&oh=00_AT-6Blak1p3MxAtVsrrihmbSEeYNnH-KXtoUWIYV7Jj63A&oe=62ED808B&_nc_sid=c504da']}
        scraped_data = self.scrape_data()
        self.assertEqual(expected_result, scraped_data[0])

if __name__ == '__main__':
    unittest.main()
