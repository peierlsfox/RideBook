//
//  Vehicle+CoreDataProperties.swift
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

extension Vehicle {

    @NSManaged var desc: String?
    @NSManaged var dimension: String?
    @NSManaged var id: String?
    @NSManaged var photo: NSData?
    @NSManaged var powerTrain: String?
    @NSManaged var suspension: String?
    @NSManaged var type: String?
    @NSManaged var project: String?
    @NSManaged var rideEvents: NSOrderedSet?
    @NSManaged var issues: Issue?
    @NSManaged var evaluateScores: NSSet?

}
