////
////  API.swift
////  PillUp
////
////  Created by Shayan on 9/16/18.
////  Copyright © 2018 Shayan. All rights reserved.
////
//
//import Foundation
//import Alamofire
//
//struct Medicine: Codable {
//    var cartridge : Int?
//    var count : Int?
//    var every : Int?
//    var id : String?
//    var last_dispense : String?
//    var name: String!
//}
//
//func getMe() {
//    Alamofire.request("http://api.pillup.org/patient/2vziI7", method: .get)
//        .responseData(completionHandler: { response in
//            let decoder = JSONDecoder()
//            let todo: Result<Medicine> = decoder.decodeResponse(from: response)
//        })
//    }
//}
//
//extension JSONDecoder {
//    func decodeResponse<T: Decodable>(from response: DataResponse<Data>) -> Result<T> {
//        guard response.error == nil else {
//            print(response.error!)
//            return .failure(response.error!)
//        }
//        
//        guard let responseData = response.data else {
//            print("didn't get any data from API")
//            return .failure()
//        }
//        
//        do {
//            let item = try decode(T.self, from: responseData)
//            return .success(item)
//        } catch {
//            print("error trying to decode response")
//            print(error)
//            return .failure(error)
//        }
//    }
//}
