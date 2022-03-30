function Activity(amount) {
  this.amount = amount 
  this.setAmount = function(value)
  {
      if(value<=0)
      {
          return false;
      }
      else{
          this.amount = value
          return true;
      }
  }
  
  this.getAmount = function()
  {
      return this.amount
  }
}



function Payment(amount, receiver) {
  Activity.call(this)
  this.amount = amount
  this.receiver = receiver;
  
  // this.setReceiver = function(value) {
  //     this.receiver = value;
  // }
  // this.getReceiver = function()
  // {
  //     return this.receiver; 
  // }
}
Payment.prototype.setReceiver = function(value)
{
  this.receiver = receiver;
}

var x1 = new Payment(2,'yoo')
console.log(Payment.prototype.hasOwnProperty('setReceiver'))