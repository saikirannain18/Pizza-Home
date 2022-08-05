
import React,{Component} from 'react';
import {Table} from 'react-bootstrap';
import "../styles/menu1.css";
 export class Menu1 extends Component{

   constructor(props){
      super(props);
      this.state={items:[],
      DataisLoaded:false};
   }

   refreshList(){
     fetch(process.env.REACT_APP_API+'Product')
     .then(response=>response.json())
     .then(data=>{
      this.setState({prods:data});
     })
   }

   componentDidMount(){
    fetch("http://127.0.0.1:8000/api/prodinfo/all/")
    .then((res) => res.json())
    .then((json) =>{
      this.setState({
        items:json,DataisLoaded: true
      });
    })
    this.refreshList();
   }

   componentDidUpdate(){
    this.refreshList();
   }

  render(){
    const {items}=this.state;

    return(
      <div >
       <Table className="Table" striped bordered hover size='sm'>
         <thead>
          <tr>
           <th>category</th>
           <th>name</th>
           <th>price</th>
           <th width="70%">image</th>
           </tr>
         </thead>
         <tbody>
           {items.map(prod=>
              <tr key={prod.name}>
                <td>{prod.category}</td>
                <td>{prod.name}</td>
                <td>{prod.price}</td>
                <td>
                  <img  src="{/uploads/product/{items.props.img}}" alt='image'  height="200px" />

                  </td>
              </tr>
            
            )}
          
          </tbody>
        </Table> 
      </div>
      
    )
  }
}
export default Menu1;