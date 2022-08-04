import React, {useState} from 'react';
import './scraper.css';
import axios from 'axios';


function App() {
  const [name, setName] = useState("");

  async function launch (){

      let data = {page_name: name}
      const url = 'http://127.0.0.1:8000/launch';
      // console.log({name});
      await axios.post(url, data).then((response) => {
          console.log(response.data);
          
        }).catch(err=>{
          console.log("error",err);
        });
        };

        
  return(
      <div className='card-container'>
          <h3 className='title1'>Facebook Page Scraper</h3>
          <form className='form'>
              <input type="text" placeholder="page name" className="name" name="page_name" onChange={(e)=>setName(e.target.value)}/>
              <button className='but2' onClick={()=>{launch()}}style={{backgroundColor:'green', color:'white', fontSize:'17px'}} >Launch</button> 
          </form>
      </div>
  )

  
}

export default App;
