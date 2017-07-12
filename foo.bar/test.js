e = document.getElementById('expander');
            flag = true
            e.addEventListener('click',(data,x) => {
                console.log(e)
               
                if(e.classList.contains('collapsed')){
                    e.classList.remove('collapsed')
                }
                else
                    e.classList.add('collapsed')
            })