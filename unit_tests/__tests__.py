import unittest
from src.main import init, listen, exec_command, tokenize, validate_command, process_sound_test
from src.executate import exec_cmd_open, exec_cmd_close, suspend

AUDIO_CHAVES = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/abrirnavegador.wav"
AUDIO_KIKO = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/kiko.wav"
AUDIO_NAVEGADOR_ABRIR = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/abrirnavegador.wav"
AUDIO_NOTAS_ABRIR = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/abrirnotas.wav"
AUDIO_MONITOR_ABRIR = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/abrirmonitor.wav"
AUDIO_NAVEGADOR_FECHAR = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/fecharnavegador.wav"
AUDIO_NOTAS_FECHAR = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/fecharnotas.wav"
AUDIO_MONITOR_FECAHR = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/fecharmonitor.wav"
AUDIO_SUSPENDER = "/Users/rafael/Desktop/inteArti/iaavaliativa/unit_tests/suspender.wav"


class TesteNomeAssistente(unittest.TestCase):
    def setUp(self):
        self.inited, self.recognizer, _, self.assistent_name, _ = init()

    def recognize_name(self):
        have_comand, comand = process_sound_test(AUDIO_CHAVES, self.recognizer)

        self.assertTrue(have_comand)

        name, _, _ = tokenize(comand)
        self.assertIsNotNone(name)
        self.assertEqual(name, self.assistent_name)

    def recognize_name_diferent(self):
        have_comand, comand = process_sound_test(AUDIO_KIKO, self.recognizer)

        self.assertTrue(have_comand)

        name, _, _ = tokenize(comand)
        self.assertIsNotNone(name)
        self.assertNotEqual(name, self.assistent_name)


class TestActions(unittest.TestCase):
    def setUp(self):
        self.inited, self.recognizer, self.stop_words, self.assistent_name, actions = init()

    def test_exec_command_open(self):
        have_comand, comand = process_sound_test(AUDIO_NOTAS_ABRIR, self.recognizer)

        self.assertTrue(have_comand)

        name, action, object = tokenize(comand)
        self.assertIsNotNone(name)
        self.assertIsNotNone(action)
        self.assertIsNotNone(object)
        self.assertEqual(name, self.assistent_name)

        valid = validate_command(action, object)

        self.assertTrue(valid)
        works = exec_command(action, comand)
        self.assertTrue(works)

    def test_exec_command_close(self):
        have_comand, comand = process_sound_test(AUDIO_NOTAS_FECHAR, self.recognizer)

        self.assertTrue(have_comand)

        name, action, object = tokenize(comand)
        self.assertIsNotNone(name)
        self.assertIsNotNone(action)
        self.assertIsNotNone(object)
        self.assertEqual(name, self.assistent_name)

        valid = validate_command(action, object)

        self.assertTrue(valid)
        works = exec_command(action, comand)
        self.assertTrue(works)

    def test_exec_command_suspend(self):
        have_comand, comand = process_sound_test(AUDIO_SUSPENDER, self.recognizer)

        self.assertTrue(have_comand)

        name, action, object = tokenize(comand)
        self.assertIsNotNone(name)
        self.assertIsNotNone(action)
        self.assertIsNotNone(object)
        self.assertEqual(name, self.assistent_name)

        valid = validate_command(action, object)

        self.assertTrue(valid)
        works = exec_command(action, comand)
        self.assertTrue(works)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()

    tests.addTest(loader.loadTestsFromTestCase(TesteNomeAssistente))
    tests.addTest(loader.loadTestsFromTestCase(TestActions))

    executor = unittest.TextTestRunner()
    executor.run(tests)