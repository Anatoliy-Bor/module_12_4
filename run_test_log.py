from runner_for_log import  Runner
import unittest
import logging



class RunnerTest(unittest.TestCase):
    is_frosen = False

    logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')


    @unittest.skipIf(is_frosen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            verification_test = Runner('Tom', -5)
            for i in range(10):
                verification_test.walk()
            self.assertEqual(verification_test.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')
            logging.error('Ошибка', exc_info=True)



    @unittest.skipIf(is_frosen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            verification_test = Runner('Ivan', -10)
            for i in range(10):
                verification_test.run()
            self.assertEqual(verification_test.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.error('Ошибка ', exc_info=True )



    @unittest.skipIf(is_frosen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj1 = Runner('Kat')
        obj2 = Runner('Anna')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == '__main__':
    unittest.main()
