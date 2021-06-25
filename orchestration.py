from nameko.rpc import RpcProxy, rpc
from nameko.events import EventDispatcher,event_handler

class OrchestrationService:
    
    name="orchestration_service"

    room_service=RpcProxy("service_room")
    booking_service=RpcProxy("booking_service")
    # palindrome_service=RpcProxy("palindrome_service")

    dispatch=EventDispatcher()

    resultgetroomtype={
        'get_room_type':None
    }

    resultgettotal={
        'get_total_room':None
    }

    resultaddroomtype={
        'add_room_type':None
    }

    resultaddroom={
        'add_room':None
    }

    resultcheckin={
        'get_checkin':None

    }

    resultcancel={
        'cancel_booking':None

    }

    resultbookingstatus={
        'book_stat':None
    }

    # #Choreography
    # @event_handler("prime_service","calculation_result_event")
    # def handle_prime_result(self,payload):
    #     self.result['is_prime']=payload

    # @event_handler("palindrome_service","calculation_result_event")
    # def handle_palindrome_result(self,payload):
    #     self.result['is_palindrome']=payload

    # @rpc
    # def is_prime_palindrome_choreo(self,num):
    #     self.dispatch("prime_palindrome_event",num)

    #     # wait for result
    #     while self.result['is_prime'] is None or self.result['is_palindrome']==None:
    #         continue
    #     self.result['is_prime_palindrome']=self.result['is_prime'] and self.result['is_palindrome']
    #     return self.result

    # pubsub
    @rpc
    def dispatch_method(self,payload):
        self.dispatch("room_event",payload)

    # orchestration
    @rpc
    # get_room_type
    def get_room_type(self):
        resultgetroomtype={
            'get_room_type':self.room_service.get_all_roomtype(),
            
        }
        return resultgetroomtype

    @rpc
    def get_total_room(self):
        resultgettotal={
            'get_total_room':self.room_service.get_count_room(),
        }
    
    @rpc
    def add_room_type(self,_name, _price, _capacity, _last_update_by):
        resultaddroomtype={
            'add_room_type':self.room_service.add_roomtype(_name, _price, _capacity, _last_update_by)
        }

    @rpc
    def add_room(self,typeid, roomnum, updateby):
        resultaddroom={
            'add_room':self.room_service.add_room(typeid, roomnum, updateby)

        }
    
    @rpc    
    def get_checkin(self,roomid):
        resultcheckin={
            'get_checkin':self.room_service.get_checkin_detail(roomid)
        }

    @rpc
    def booking_status(self, type_id, idlogin):
        resultbookingstatus={
            'book_stat':self.booking_service.update_booking_status_from_room(type_id,idlogin)
        }
        return resultbookingstatus



    @rpc
    def cancel_booking(self, idbooking, idroom, idlogin):
       resultcancel = {
        #    'cancel_room': self.service_room.update_cancel_room(idroom, idlogin),
        #    'booking_status': self.booking_service.update_booking_status(idbooking),
           'cancel_booking' : self.room_service.update_cancel_room(idroom, idlogin) and self.booking_service.update_booking_status(idbooking, idlogin)

       }

       return "berhasil : " + result

