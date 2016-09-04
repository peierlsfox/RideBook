//
//  RideDataManager.swift
//  RideBook
//
//  Created by hupei on 16/5/19.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit
import CoreData

class RideDataManager: NSObject {
    let context:NSManagedObjectContext
    let vehicleEntityName:String
    
    static let sharedInstance=RideDataManager()
    
    private override init() {
        context = (UIApplication.sharedApplication().delegate as! AppDelegate).managedObjectContext
        vehicleEntityName="Vehicle"
    }

    func addEvaluateItem(evalItem:EvaluateItem){
        
    }
    
    func createNewVehicle()->Vehicle{
        let entityName="Vehicle"
        let entity=NSEntityDescription.entityForName(entityName, inManagedObjectContext: context)
        let vehicle=Vehicle(entity:entity!,insertIntoManagedObjectContext:context)
        
        vehicle.id="未编号"
        vehicle.desc="无描述"
        
        return vehicle
    }
    
    func getVehicle(vehicleId:String)->Vehicle?{
        let fetchRequest=NSFetchRequest(entityName: vehicleEntityName)
        fetchRequest.predicate=NSPredicate(format: "id == %@", vehicleId)
        do {
            let result=try context.executeFetchRequest(fetchRequest)
            if result.count>0{
                return result[0] as? Vehicle
            }
        }catch{
            print(NSError.description())
        }
        return nil
    }
    
}
