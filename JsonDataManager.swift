//
//  JsonDataManager.swift
//  RideBook
//
//  Created by hupei on 16/5/29.
//  Copyright © 2016年 hupei. All rights reserved.
//

import Foundation
import CoreData
import UIKit

class JsonDataManager:NSObject{
    
    func importJSONSeedDataIfNeeded(coreDataStack:CoreDataStack) {
        
        let fetchRequest = NSFetchRequest(entityName: "RideEvent")
        var error:NSError? = nil
        
        let count = coreDataStack.context
            .countForFetchRequest(fetchRequest, error: &error)
        
        if count == 0 {
            importJSONDataForRideEvent(coreDataStack)
            importJSONDataForVehicle(coreDataStack)
            importJSONDataForGroupAndPerson(coreDataStack)
            importJSONDataForEvaluateItems(coreDataStack)
        }
    }
    
    func importJSONDataForRideEvent(coreDataStack:CoreDataStack) {
        let jsonURL = NSBundle.mainBundle().URLForResource("rideEvent", withExtension: "json")
        let jsonData = NSData(contentsOfURL: jsonURL!)
        
        do {
            let jsonArray = try NSJSONSerialization.JSONObjectWithData(jsonData!, options: .AllowFragments) as! NSArray
            let entity = NSEntityDescription.entityForName("RideEvent", inManagedObjectContext: coreDataStack.context)
            
            for jsonDictionary in jsonArray {
                let date = jsonDictionary["date"] as! String
                let location = jsonDictionary["location"] as! String
                let name = jsonDictionary["name"] as! String
                let remark = jsonDictionary["remark"] as! String
                
                let rideEvent = RideEvent(entity: entity!,
                                insertIntoManagedObjectContext: coreDataStack.context)
                
                let dateFormatter = NSDateFormatter()
                dateFormatter.dateFromString("yyyy-MM-dd")
                
                rideEvent.date = dateFormatter.dateFromString(date)
                rideEvent.name = name
                rideEvent.location = location
                rideEvent.remark = remark
            }
            
            coreDataStack.saveContext()
            print("Imported \(jsonArray.count) ride event")
            
        } catch let error as NSError {
            print("Error importing a ride event: \(error)")
        }
    }
    
    func importJSONDataForVehicle(coreDataStack:CoreDataStack) {
        let jsonURL = NSBundle.mainBundle().URLForResource("vehicles", withExtension: "json")
        let jsonData = NSData(contentsOfURL: jsonURL!)
        
        do {
            let jsonArray = try NSJSONSerialization.JSONObjectWithData(jsonData!, options: .AllowFragments) as! NSArray
            let entity = NSEntityDescription.entityForName("Vehicle", inManagedObjectContext: coreDataStack.context)
            
            for jsonDictionary in jsonArray {
                let desc = jsonDictionary["desc"] as! String
                let id = jsonDictionary["id"] as! String
                let powerTrain = jsonDictionary["powerTrain"] as! String
                let suspension = jsonDictionary["suspension"] as! String
                let dimension = jsonDictionary["dimension"] as! String
                //let photoName = jsonDictionary["photo"] as! String
                
                let vehicle = Vehicle(entity: entity!,
                                          insertIntoManagedObjectContext: coreDataStack.context)
                
                vehicle.desc = desc
                vehicle.id = id
                vehicle.powerTrain = powerTrain
                vehicle.suspension = suspension
                vehicle.dimension = dimension
                
                //let image=UIImage(named: photoName)
                //let photoData=UIImagePNGRepresentation(image!)
                //vehicle.photo=photoData

            }
            
            coreDataStack.saveContext()
            print("Imported \(jsonArray.count) vehicles")
            
        } catch let error as NSError {
            print("Error importing vehicles: \(error)")
        }
    }
    
    func importJSONDataForEvaluateItems(coreDataStack:CoreDataStack) {
        let jsonURL = NSBundle.mainBundle().URLForResource("items", withExtension: "json")
        let jsonData = NSData(contentsOfURL: jsonURL!)
        
        do {
            let jsonArray = try NSJSONSerialization.JSONObjectWithData(jsonData!, options: .AllowFragments) as! NSArray
            let entity = NSEntityDescription.entityForName("EvaluateItem", inManagedObjectContext: coreDataStack.context)
            

            
            for jsonDictionary in jsonArray {
                let desc = jsonDictionary["desc"] as! String
                let itemCode = jsonDictionary["itemCode"] as! String
                let mainSection = jsonDictionary["mainSection"] as! String
                let order = jsonDictionary["order"] as! NSNumber
                let rank = jsonDictionary["rank"] as! NSNumber
                let remark = jsonDictionary["remark"] as! String
                let title=jsonDictionary["title"] as! String
                
                let item = EvaluateItem(entity: entity!,
                                      insertIntoManagedObjectContext: coreDataStack.context)
                
                item.desc=desc
                item.itemCode=itemCode
                item.mainSection=mainSection
                item.order=order
                item.rank=rank
                item.remark=remark
                item.title=title
                
            }
            
            coreDataStack.saveContext()
            print("Imported \(jsonArray.count) evaluation items")
            
        } catch let error as NSError {
            print("Error importing evaluation items: \(error)")
        }
    }
    
    func importJSONDataForGroupAndPerson(coreDataStack:CoreDataStack) {
        let jsonURL = NSBundle.mainBundle().URLForResource("groups", withExtension: "json")
        let jsonData = NSData(contentsOfURL: jsonURL!)
        
        do {
            let jsonArray = try NSJSONSerialization.JSONObjectWithData(jsonData!, options: .AllowFragments) as! NSArray
            let entity = NSEntityDescription.entityForName("Group", inManagedObjectContext: coreDataStack.context)
            
            for jsonDictionary in jsonArray {
                let name = jsonDictionary["name"] as! String
                let remark = jsonDictionary["remark"] as! String
                let index = jsonDictionary["index"] as! NSNumber
                
                let group = Group(entity: entity!,insertIntoManagedObjectContext: coreDataStack.context)
                
                group.name=name
                group.remark=remark
                group.index=index
                
                let attendances=NSMutableOrderedSet()
                let personsArray=jsonDictionary["persons"] as! NSArray
                let entityPerson=NSEntityDescription.entityForName("Person", inManagedObjectContext: coreDataStack.context)
                let entityAttendance=NSEntityDescription.entityForName("Attendance", inManagedObjectContext: coreDataStack.context)
                
                for jsonPersonDic in personsArray{
                    let name=jsonPersonDic["name"] as! String
                    let position=jsonPersonDic["position"] as! String
                    //let photoName=jsonPersonDic["photo"] as! String
                    
                    let person=Person(entity: entityPerson!,insertIntoManagedObjectContext: coreDataStack.context)
                    let attendance=Attendance(entity: entityAttendance!, insertIntoManagedObjectContext: coreDataStack.context)
                    
                    person.name=name
                    person.position=position
                    
                    attendance.person=person
                    attendance.group=group
                    
                    //let image=UIImage(named: photoName)
                    //let photoData=UIImagePNGRepresentation(image!)
                    //person.photo=photoData
                    attendances.addObject(attendance)
                }
                group.attendances=attendances.copy() as? NSOrderedSet
            }
            
            coreDataStack.saveContext()
            print("Imported \(jsonArray.count) groups")
            
        } catch let error as NSError {
            print("Error importing groups: \(error)")
        }
    }

}