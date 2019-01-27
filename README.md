# approvico

# Type 1 : zero waiting with preset condition of approval

import "Google Vision" as gv
import "Microsoft Coputer Vision" as mcv
import "EXIFtool" as ex

function get_approval (image) {

  parsed_data = parse_receipt(image) 
  
  BOOLEAN approval = verify(parsed_data) // e.g. date_time_transaction - date_time_image < 3.hours */
  
    return BOOLEAN approval
  }

}


function parse_receipt (binary image) {

  gv.parse(image)
  mcv.parse(image)
  ex.parse(image)

  return JSON parsed_data = {
      total_amount = <float>,
      coordinate_transaction: <string>, 
      coordinate_image: <string>,
      date_time_transaction: <datetime>,
      date_time_image: <datetime>
    }
  
  }



