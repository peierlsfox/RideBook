//
//  EvaluateScore+CoreDataProperties.swift
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

extension EvaluateScore {

    @NSManaged var rank: NSNumber?
    @NSManaged var comments: String?
    @NSManaged var evaluateItem: EvaluateItem?
    @NSManaged var rideEvent: RideEvent?
    @NSManaged var person: Person?
    @NSManaged var vehicle: Vehicle?
    @NSManaged var evaluateScores: NSSet?
    @NSManaged var issues: NSSet?

}
