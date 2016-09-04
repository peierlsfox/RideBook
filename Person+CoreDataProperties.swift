//
//  Person+CoreDataProperties.swift
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

extension Person {

    @NSManaged var name: String?
    @NSManaged var photo: NSData?
    @NSManaged var position: String?
    @NSManaged var attendances: NSOrderedSet?
    @NSManaged var issues: NSSet?
    @NSManaged var evaluateRecordes: NSSet?

}
