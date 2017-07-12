cont = 0
function grid(x,y,rows,cols,enemy = null, player = null, box_width = 1){
    this.x = x;
    this.y = y;
    this.rows = rows;
    this.cols = cols;
    this.enemy = enemy
    this.player = player
    this.box_width = box_width;
    this.draw = function(){
        // console.log(this.rows,this.cols, this.count)
        tmp = 0
        for(i = 0; i <= this.cols;i++){
            line(this.x+tmp, this.y, this.x+tmp, this.y +(this.rows * this.box_width));
            tmp += this.box_width;
        }
        tmp = 0
        
        for(i = 0; i <= this.rows;i++){
            line(this.x, this.y + tmp, this.x + (this.cols * this.box_width), this.y + tmp);
            tmp += this.box_width;
        }
       
        if(this.enemy != null){
            stroke(255,0,0)
            strokeWeight(10)
            point(this.x + this.enemy[0]*this.box_width,this.y + this.enemy[1]*this.box_width)
            stroke(0)
            strokeWeight(1)
        }
        if(this.player != null){
            stroke(0,255,0)
            strokeWeight(10)
            point(this.x + this.player[0]*this.box_width,this.y + this.player[1]*this.box_width)
            stroke(0)
            strokeWeight(1)
        }
        
    }
    
    this.top = function(){
        x =  new grid(this.x, this.y - this.box_width * this.rows,
        this.rows,this.cols, [this.enemy[0], this.rows -this.enemy[1]], 
        [this.rows - this.player[0], this.player[1]]
        )
     
        return x
    }
    this.left = function(){
        x =  new grid(this.x - this.box_width * this.cols, this.y ,
        this.rows,this.cols, [this.cols - this.enemy[0], this.enemy[1]],
        [this.cols - this.player[0], this.player[1]])
     
        return x
    }
    this.bottom = function(){
        x =  new grid(this.x, this.y + this.box_width * this.rows,
        this.rows,this.cols, [this.enemy[0], this.rows -this.enemy[1]],
        [this.player[0], this.rows -this.player[1]])
     
        return x
    }
    this.right =  function(){
        x =  new grid(this.x + this.box_width * this.cols, this.y ,
        this.rows,this.cols, [this.cols - this.enemy[0], this.enemy[1]],
        [this.player[0], this.cols -this.player[1]])
        console.log(this.cols - this.enemy[0], this.enemy[1])
        return x
    }

}
ds = {}

function dl(parent, child){
    x1 = parent.x + parent.box_width * parent.player[0];
    y1 = parent.y + parent.box_width * parent.player[1];
    x2 = child.x + parent.box_width * child.enemy[0];
    y2 = child.y + parent.box_width * child.enemy[1];
    x3 = child.x + parent.box_width * child.player[0];
    y3 = child.y + parent.box_width * child.player[1];
    if (x1 - x2 == 0){
        ds["u"] = 0
        console.log("undefined")
    }else{
        ds[(y2 - y1)/(x2 - x1)] = true
       console.log(Math.atan((y2 - y1)/(x2 - x1)), Math.sqrt(Math.pow((y2 - y1),2) + Math.pow(x2 - x1,2)),x2, y2)
    }
    stroke(0,0,255)
    strokeWeight(3)
    line(x1,y1,x2,y2)
    line(x1,y1,x3,y3)
    stroke(0)
            strokeWeight(1)
}

function len(x){
    count = 0
    for(i in x){
         ++count
         console.log(count, i)
    }
    return count
}
function setup(){
    createCanvas(1000,1000)
    background(244)
    x = new grid(500,500, 59,42, [6,34],[34,44]);
    stroke(2)
    t = x.top()
    t.draw()
    l  = x.left()
    l.draw()
    r = x.right()
    r.draw()
    b = x.bottom()
    b.draw()
    br = b.right()
    br.draw()
    bl = b.left()
    bl.draw()
    tl = t.left()
    tl.draw()
    tr = t.right()
    tr.draw()


    trt = tr.top()
    trt.draw()
    tt = t.top()
    tt.draw()
    tlt = tl.top()
    tlt.draw()
    dl(x,trt)
    trtr = trt.right()
    trtr.draw()
    dl(x,trtr)
    trr = tr.right()
    trr.draw()
    rr = r.right()
    rr.draw()

    brr = br.right()
    brr.draw()
    dl(x,brr)
    dl(x,rr)
    dl(x,trr)
    
    strokeWeight(2)
    stroke(120,0,255)
    x.draw()
    
    dl(x,x)
    dl(x,t)
    dl(x,tr)
    dl(x,r)
    dl(x,bl)
    dl(x,b)
    dl(x,br)
    dl(x,tl)
    dl(x,l)
    
}
function draw(){
 
    



  
}