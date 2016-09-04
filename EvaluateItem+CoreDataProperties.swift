//
//  EvaluateItem+CoreDataProperties.swift
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

extension EvaluateItem {

    @NSManaged var desc: String?
    @NSManaged var itemCode: String?
    @NSManaged var mainSection: String?
    @NSManaged var order: NSNumber?
    @NSManaged var rank: NSNumber?
    @NSManaged var remark: String?
    @NSManaged var title: String?
    @NSManaged var rideEvent: RideEvent?
    @NSManaged var scores: NSSet?

}
