async function modd_n() {
    let p = document.getElementById('location2').value;
    let q = document.getElementById('location3').value;
    
    
    let e_c = await eel.generate_key_pair(p, q)();
    if (e_c == 'ValueError') {
        document.getElementById('einf').innerHTML = 'Введите корректные данные'
    } else {
        document.getElementById('info').innerHTML = 'Открытый ключ:' + '\n' + 'e = ' + e_c[0][0] + ' ' + 'n = ' + e_c[0][1] + '\n\n' + 'Cекретный ключ:' + '\n' + 'd = ' + e_c[1][0];
        document.getElementById('einf').innerHTML = ''
    }
}

document.getElementById('get').addEventListener('click', modd_n);