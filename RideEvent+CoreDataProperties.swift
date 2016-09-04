//
//  RideEvent+CoreDataProperties.swift
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

extension RideEvent {

    @NSManaged var date: NSDate?
    @NSManaged var location: String?
    @NSManaged var name: String?
    @NSManaged var remark: String?
    @NSManaged var project: String?
    @NSManaged var groups: NSOrderedSet?
    @NSManaged var items: NSOrderedSet?
    @NSManaged var vehicles: NSOrderedSet?
    @NSManaged var issues: NSOrderedSet?
    @NSManaged var evaluateScores: NSOrderedSet?

}
