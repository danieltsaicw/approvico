
ref of django https://django.readthedocs.io/en/2.1.x/intro/tutorial01.html




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

# Type 2 : waiting with manual approval from supervisors



function get_approval (image) {

  parsed_data = parse_receipt(image) 
  
  BOOLEAN approval = verify(parsed_data) // e.g. date_time_transaction - date_time_image < 3.hours */

    <method 2-1>
      email_superivsor = email_mapping_list(email_address_staff)
      approval = mailer.send()
    </method 2-1>

    <method 2-2>
      blochchain_address_approver = blockchain_address_mapping_list(blockchain_address_staff)
      blockchain_notification(blochchain_address_approver) @Puranj, HOW? There's no way to build eamil server on chain 
      approval = waiting (feeback_approver) @Puranj, what's the data type of the feedback from approver?
    </method 2-2>

    return BOOLEAN approval
  }

}

# updates of Credibity token


  if supervisor approves 
  then Approvee.at("blockchain_address").creditibyt += 1
  



# save into blockchian

what to save?
why save on chain rather than on sever?


# read from blockchain

who would read?
what moivates them to read?

# other issues
supervisors has no incentive to approve (only approvee get Credibity Token)






