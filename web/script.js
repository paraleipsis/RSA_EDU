function is_numeric(str){
    return /^\d+$/.test(str);
}

const count = (arr) => arr.reduce((acc, num) => acc + num, 0);

async function modd_n() {
    let p = document.getElementById('location2').value;
    let q = document.getElementById('location3').value;
    let m = document.getElementById('location').value;
    if (p == '' || q == '' || is_numeric(q) || m == '' || is_numeric(m)) {
        document.getElementById('einf').innerHTML = 'Введите корректные данные';
        document.getElementById('einf1').innerHTML = '';
    } else {
        let e_c = await eel.generate_key_pair(p, q)();
        let m_c = await eel.m_encrypt(m)();
        if (e_c == 'ValueError' || e_c[2].length == 0) {
            document.getElementById('einf').innerHTML = 'Введите корректные данные';
            document.getElementById('einf1').innerHTML = '';
        } else {
            t = e_c[2].join(' ');
            t1 = m_c[1].join(' '); 
            document.getElementById('einf1').innerHTML = `Вычисляемое число p:<br \/>p = ${e_c[3]}<br \/><br \/>Последовательность чисел:<br \/>${t}<br \/><br \/>Сумма последовательности чисел:<br \/>${count(e_c[2])}<br \/><br \/>Наиболее близкое простое число:<br \/>q = ${e_c[4]}<br \/><br \/>Произведение p и q :<br \/>n = ${e_c[5]}<br \/><br \/>Функция Эйлера:<br \/>\u03C6 = ${e_c[6]}<br \/><br \/>Открытый ключ:<br \/>e = ${e_c[0][0]} n = ${e_c[0][1]}<br \/><br \/>Cекретный ключ:<br \/>d = ${e_c[1]}<br \/><br \/>Первые 5 букв шифруемого текста:<br \/>m = ${m_c[0]}<br \/><br \/>Числовое отображение шифруемого текста:<br \/>${t1}`;
            document.getElementById('einf').innerHTML = '';
        }
    }
}

document.getElementById('get').addEventListener('click', modd_n);