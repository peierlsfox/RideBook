//
//  personViewController.swift
//  RideBook
//
//  Created by hupei on 16/5/29.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit
import CoreData

class PersonViewController: UIViewController {
    
    @IBOutlet weak var tableView: UITableView!
    var coreDataStack: CoreDataStack!
    
    var fetchedResultsController:NSFetchedResultsController!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title="出席管理"
        
        //1
        let fetchRequest = NSFetchRequest(entityName: "Attendance")
        //fetchRequest.predicate=NSPredicate(format: <#T##String#>, <#T##args: CVarArgType...##CVarArgType#>)
        
        let sectionSort =
           NSSortDescriptor(key: "group.name", ascending: true)
        
        let orderSort =
            NSSortDescriptor(key: "person.name", ascending: true)
        
        fetchRequest.sortDescriptors = [sectionSort,orderSort]
        
        //2
        fetchedResultsController =
            NSFetchedResultsController(fetchRequest: fetchRequest,
                                       managedObjectContext: coreDataStack.context,
                                       sectionNameKeyPath: "group.name",
                                       cacheName: "PersonResult")
        
        //fetchedResultsController.delegate = self
        
        //3
        do {
            try fetchedResultsController.performFetch()
        } catch let error as NSError {
            print("Error: \(error.localizedDescription)")
        }
        
    }
    
    func configureCell(cell: PersonViewCell, indexPath: NSIndexPath) {
        let attendance=fetchedResultsController.objectAtIndexPath(indexPath) as! Attendance
        cell.nameLabel.text=attendance.person!.name!
        cell.positionLabel.text=attendance.person!.position!
    }
    
    
}

extension PersonViewController:UITableViewDataSource{
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return fetchedResultsController.sections!.count
    }
    
    func tableView(tableView: UITableView,titleForHeaderInSection section: Int) -> String? {
        let sectionInfo = fetchedResultsController.sections![section]
        return sectionInfo.name
    }
    
    func tableView(tableView: UITableView,numberOfRowsInSection section: Int) -> Int {
        let sectionInfo = fetchedResultsController.sections![section]
        return sectionInfo.numberOfObjects
    }
    
    func tableView(tableView: UITableView,cellForRowAtIndexPath indexPath: NSIndexPath)-> UITableViewCell {
        
        let cell = tableView.dequeueReusableCellWithIdentifier("personCell", forIndexPath: indexPath)
            as! PersonViewCell
        
        configureCell(cell, indexPath: indexPath)
        
        return cell
    }
    
}
