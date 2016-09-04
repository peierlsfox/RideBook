//
//  VehicleViewController.swift
//  RideBook
//
//  Created by hupei on 16/5/30.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit
import CoreData

class VehicleViewController: UIViewController {

    @IBOutlet weak var tableView: UITableView!
    
    var coreDataStack: CoreDataStack!
    
    var fetchedResultsController:NSFetchedResultsController!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title="车辆管理"
        
        //1
        let fetchRequest = NSFetchRequest(entityName: "Vehicle")
        //fetchRequest.predicate=NSPredicate(format: <#T##String#>, <#T##args: CVarArgType...##CVarArgType#>)
        
        //let sectionSort =
        //    NSSortDescriptor(key: "id", ascending: true)
        
        let orderSort =
            NSSortDescriptor(key: "id", ascending: true)
        
        fetchRequest.sortDescriptors = [orderSort]
        
        //2
        fetchedResultsController =
            NSFetchedResultsController(fetchRequest: fetchRequest,
                                       managedObjectContext: coreDataStack.context,
                                       sectionNameKeyPath: nil,
                                       cacheName: nil)
        
        //fetchedResultsController.delegate = self
        
        //3
        do {
            try fetchedResultsController.performFetch()
        } catch let error as NSError {
            print("Error: \(error.localizedDescription)")
        }
        
    }
    
    func configureCell(cell: VehicleViewCell, indexPath: NSIndexPath) {
        let vehicle=fetchedResultsController.objectAtIndexPath(indexPath) as! Vehicle
        cell.noLabel.text=vehicle.id
        cell.descLabel.text=vehicle.desc
        cell.detailLabel.text=" \(vehicle.powerTrain!) \r \(vehicle.suspension!) \r \(vehicle.dimension!)"
    }
    
    
}

extension VehicleViewController:UITableViewDataSource{
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
        
        let cell = tableView.dequeueReusableCellWithIdentifier("vehicleCell", forIndexPath: indexPath)
            as! VehicleViewCell
        
        configureCell(cell, indexPath: indexPath)
        
        return cell
    }
    
}

