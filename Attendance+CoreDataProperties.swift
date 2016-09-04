//
//  Attendance+CoreDataProperties.swift
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

extension Attendance {

    @NSManaged var isAttended: NSNumber?
    @NSManaged var remark: String?
    @NSManaged var group: Group?
    @NSManaged var person: Person?

}
