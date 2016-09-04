//
//  Issue+CoreDataProperties.swift
//  RideBook
//
//  Created by hupei on 16/6/2.
//  Copyright © 2016年 hupei. All rights reserved.
//
//  Choose "Create NSManagedObject Subclass…" from the Core Data editor menu
//  to delete and recreate this implementation file for your updated model.
//

import Foundation
import CoreData

extension Issue {

    @NSManaged var type: String?
    @NSManaged var title: String?
    @NSManaged var openDate: NSDate?
    @NSManaged var details: String?
    @NSManaged var vehicle: Vehicle?
    @NSManaged var rideEvent: RideEvent?
    @NSManaged var issuer: Person?
    @NSManaged var evaluateScore: EvaluateScore?

}
