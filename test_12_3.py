import runner_and_tournament as rt
import unittest
import runner

#Создаем класс для тестов:
    
class RunnerTest(unittest.TestCase):
    is_frozen = False
    
#Создаем тест работы функции 'walk' относительно рассчитанного значения:
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        first_walker = runner.Runner('Bob')
        for i in range(10):
            runner.Runner.walk(first_walker)
        distance_first_walker = first_walker.distance
        self.assertEqual(distance_first_walker, 50, 'Fail')

#Создаем тест работы функции 'run' относительно рассчитанного значения: 
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')                         
    def test_runner(self):
        first_runner = runner.Runner('Petr')
        for i in range(10):
            runner.Runner.run(first_runner)
        distance_first_runner = first_runner.distance
        self.assertEqual(distance_first_runner, 100, 'Fail')
       
#Создаем тест работы функций 'walk' и 'run' относительно друг друга:
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')     
    def test_challenge(self):
        sec_walker = runner.Runner('Vasya')
        for i in range(10):
            runner.Runner.walk(sec_walker)
        distance_sec_walker = sec_walker.distance
        sec_runner = runner.Runner('Georgy')
        for i in range(10):
            runner.Runner.run(sec_runner)
        distance_sec_runner = sec_runner.distance
        self.assertNotEqual(distance_sec_walker, distance_sec_runner, 'Fail')

#Создаем класс для теста турниров:
class TournamentTest(unittest.TestCase):
    is_frozen = True
    
#Содаем функцию, создающую список для хранения результатов всех турниров. Данная функция выполняется 1 раз до начала турниров:
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        
#Создаем функцию для создания объектов-участников турниров:
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')    
    def setUp(self):
        self.r1 = rt.Runner('Усейн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)
       
#Создаем функцию для вывода в консоль результатоы каждого турнира построчно. Данная функция выполняется 1 раз после всех турниров:
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    
#Функция, имитирующая турнир 1:
    def test_running1(self):
        Tournament1 = rt.Tournament(90, self.r1, self.r3)
        end_r = len(Tournament1.participants)
        self.results = Tournament1.start()
        self.all_results.append({key: value.name for key, value in self.results.items()})
        self.assertTrue(self.results[end_r] == 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    
#Функция, имитирующая турнир 2:
    def test_running2(self):
        Tournament2 = rt.Tournament(90, self.r2, self.r3)
        end_r = len(Tournament2.participants)
        self.results = Tournament2.start()
        self.all_results.append({key: value.name for key, value in self.results.items()})
        self.assertTrue(self.results[end_r] == 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    
#Функция, имитирующая турнир 3:
    def test_running3(self):
        Tournament3 = rt.Tournament(90, self.r2, self.r1, self.r3)
        end_r = len(Tournament3.participants)
        self.results = Tournament3.start()
        self.all_results.append({key: value.name
        for key, value in self.results.items()})
        self.assertTrue(self.results[end_r] == 'Ник')
        
#Запускаем код при условии, что он запущен из модуля тестирования:      
if __name__ == '__main__':
    unittest.main()