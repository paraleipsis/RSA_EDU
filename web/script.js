async function modd_n() {
    let p = document.getElementById('location2').value;
    let q = document.getElementById('location3').value;
    
    while (true) {
        let e = document.getElementById('location4').value;
        let e_c = await eel.e_check(q, p, e)();
        if (e_c == true) {
            document.getElementById('info').innerHTML = e;
            break;
        } else {
            e = 'no'
            document.getElementById('einf').innerHTML = e;
            continue;
        }
    }

}

document.getElementById('get').addEventListener('click', modd_n);