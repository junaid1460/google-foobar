let first_array = [
    {
        name: 'John',
        age: 40,
        hide: true,
        childs: [
            {
                name: 'Alice',
                age: 20,
                hide: false,
                childs: [
                    {
                        name: 'Mike',
                        age: 2,
                        hide: true
                    }
                ]
            }
        ]
    },
    {
        name: 'Peter',
        age: 40,
        hide: true,
        childs: [
            {
                name: 'Andrew',
                age: 20,
                hide: true,
                childs: [
                    {
                        name: 'Jessica',
                        age: 2,
                        hide: true
                    }
                ]
            }
        ]
            
    }
]

let second_array = [
    {
        name: 'John',
        age: 40,
        childs: [
            {
                name: 'Alice',
                age: 20,
                childs: [
                    {
                        name: 'Mike',
                        age: 2,
                    }
                ]
            }
        ]
    },
    {
        name: 'Peter',
        age: 40,
        childs: [
            {
                name: 'Andrew',
                age: 20,
                childs: [
                    {
                        name: 'Jessica',
                        age: 2,
                    }
                ]
            }
        ]
    }
]
function getHideProperty(first = [], second ) {
    var childs = [] //this is what you are going to return
    
    for (fi in first) {
        f = first[fi]
        for (si in second) {
            s = second[si]
            if (s.name === f.name) {
                var temp = f.constructor()
                for(i in f) if(i !='childs') temp[i] = f[i]
                if (s.childs && f.childs) {
                    temp ['childs'] = getHideProperty(f.childs, s.childs)
                }
                
                childs.push(temp)
            }
        }
    }
    return childs
}

console.log(getHideProperty(first_array,second_array))