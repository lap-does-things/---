from tokenize import tokenize, untokenize
import sys 
ver="ХУЙ - Хороший, Удобный, Интерпретируемый. v.1.0"

'''

ХУЙ - Хороший, Удобный, Интерпретируемый. v.1.0
Этот интерпретатор Python был сильно вдохновлён YoptaScript 
И был сделан из лени автора.

Чтобы запустить на нём хоть что-то, закиньте этот файл в папку с вашим кодом и пропишите 

python hui.py [имя файла\путь к файлу в подпапках]

Сделал Лэпчик, Unproductive Lab ебанулись

'''

'''
    Ниже находятся ключевые слова и их сородичи из Питона :
'''

def runit(file : str):
    keys={
        "ошибка":"Exception",
        "пожалуйста":"if True:", 
# таким образом, пожалуйста ничего не делает, только вы становитесь приличнее
        "нет":"False",
        "пусто":"None",
        "да":"True",
        "и":"and",
        "как":"as",
        "обязательно":"assert",
        "прекратить":"break",
        "класс":"class",
        "дальше":"continue",
        "функция":"def",
        "удалить":"del",
        "ели же":"elif",
        "иначе":"else",
        "только":"except",
        "в конце концов":"finally",
        "до тех пор пока":"for",
        "из":"from",
        "везде":"global",
        "если":"if",
        "спиздить":"import",
        "в":"in",
        "это":"is",
        "лямбда":"lambda",
        "вездешний":"nonlocal",
        "не":"not",
        "или":"or",
        "похуй":"pass",
        "пояснить":"raise",
        "отдать":"return",
        "попробовать":"try",
        "пока":"while",
        "с":"with",
        "выдать":"yield",
        "модуль":"abs",
        "все":"all",
        "хз":"any",
        "аскии":"ascii",
        "двоичка":"bin",
        "данет":"bool",
        "буква":"chr",
        "отдатьметод":"classmethod",
        "нахуйключи":"enumerate",
        "питонить":"eval",
        "фильтр":"filter",
        "помогите":"help",
        "айди":"id",
        "вход":"input",
        "чисто":"int",
        "подкласс":"issubclass",
        "длина":"len",
        "применить":"map",
        "макс":"max",
        "память":"memoryview",
        "мин":"min",
        "открыть":"open",
        "юникод":"ord",
        "степень":"pow",
        "вывод":"print",
        "диапазоне":"range",
        "округлить":"round",
        "сортировать":"sorted",
        "безклассрвый":"staticmethod",
        "сумма":"sum",
        "отцовский":"super",
        "констсписок":"tuple",
        "связать":"zip",
        "чтоэтоблятьтакое":"print(ver)",
        "поясняю":"#"
    }

    with open(file, 'rb') as src:
        tokens=[]
        for token in tokenize(src.readline):
            if token.string in keys:
                t = (token.type, keys[token.string])
            else: t= (token.type, token.string)
            
            tokens.append(t)

    code = untokenize(tokens).decode("utf-8")
    exec(code)


if __name__ == '__main__':
    runit(file=sys.argv[1])