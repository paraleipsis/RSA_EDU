async function modd_n() {
    let p = document.getElementById('location2').value;
    let q = document.getElementById('location3').value;
    
    
    let e_c = await eel.generate_key_pair(p, q)();
    document.getElementById('info').innerHTML = e_c;
            

}

document.getElementById('get').addEventListener('click', modd_n);