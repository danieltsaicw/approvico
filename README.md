# approvico




import "Google Vision" as gv
import "Microsoft Coputer Vision" as mcv
import "EXIFtool" as ex

function get_approval (image) {

  parsed_data = parse_receipt(image) 
  
  BOOLEAN approval = verify(parsed_data) // e.g. date_time_transaction - date_time_image < 3.hours */
  
    return BOOLEAN approval
  }

}


function parse_receipt (image) {

  gv.parse(image)
  mcv.parse(image)
  ex.parse(image)

  return JSON parsed_data = {
      total_amount: FLOAT, <br>
      coordinate_transaction: STRING, <br> 
      coordinate_image: STRING, <br>
      date_time_transaction: STRING, <br>
      date_time_image: DATETIME <br>
    }
  
  }

# Type 2 : zero waiting with preset condition of approval



function get_approval (image) {

  parsed_data = parse_receipt(image) 
  
  BOOLEAN approval = verify(parsed_data) // e.g. date_time_transaction - date_time_image < 3.hours */
  
    return BOOLEAN approval
  }

}








