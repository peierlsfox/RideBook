//
//  ViewController.swift
//  RideBook
//
//  Created by hupei on 16/5/17.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit
import CoreData

class ItemViewController: UIViewController {

    @IBOutlet weak var tableView: UITableView!
    var coreDataStack: CoreDataStack!
    
    var fetchedResultsController:NSFetchedResultsController!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        createTestDataIfEmpty()
        title="评估条目"
        //tableView.registerClass(ItemViewCell.self, forCellReuseIdentifier: "itemCell")
        
        //1
        let fetchRequest = NSFetchRequest(entityName: "EvaluateItem")
        //fetchRequest.predicate=NSPredicate(format: <#T##String#>, <#T##args: CVarArgType...##CVarArgType#>)
        
        let sectionSort =
            NSSortDescriptor(key: "mainSection", ascending: true)
        let orderSort =
            NSSortDescriptor(key: "order", ascending: true)
        
        fetchRequest.sortDescriptors = [sectionSort, orderSort]
        
        //2
        fetchedResultsController =
            NSFetchedResultsController(fetchRequest: fetchRequest,
                                       managedObjectContext: coreDataStack.context,
                                       sectionNameKeyPath: "mainSection",
                                       cacheName: "EvaluationResult")
        
        //fetchedResultsController.delegate = self
        
        //3
        do {
            try fetchedResultsController.performFetch()
        } catch let error as NSError {
            print("Error: \(error.localizedDescription)")
        }

        
        
    }

    func createTestDataIfEmpty(){
        let itemEntity=NSEntityDescription.entityForName("EvaluateItem", inManagedObjectContext: coreDataStack.context)
        let fetchRequest = NSFetchRequest(entityName: "EvaluateItem")
        do{
            let results=try coreDataStack.context.executeFetchRequest(fetchRequest)
            if results.count>0 {
                return
            }else{
                let item1=EvaluateItem(entity: itemEntity!, insertIntoManagedObjectContext: coreDataStack.context)
                item1.desc="低速加速性能"
                item1.mainSection="动力性"
                item1.order=NSNumber(integer: 1)
                item1.rank=NSNumber(double: 5.5)
                item1.itemCode="1.1"
                item1.remark="冲击大"
                
                let item2=EvaluateItem(entity: itemEntity!, insertIntoManagedObjectContext: coreDataStack.context)
                item2.desc="高速加速性能"
                item2.mainSection="动力性"
                item2.order=NSNumber(integer: 2)
                item2.rank=NSNumber(double: 7.5)
                item2.itemCode="1.2"
                
                let item3=EvaluateItem(entity: itemEntity!, insertIntoManagedObjectContext: coreDataStack.context)
                item3.desc="加速时噪音"
                item3.mainSection="噪音"
                item3.order=NSNumber(integer: 1)
                item3.rank=NSNumber(double: 7.5)
                item3.itemCode="2.1"
                item3.remark="语音清晰度高"
                
                coreDataStack.saveContext()
                
            }
        }catch let error as NSError{
            print("Error: \(error) " +
                "description \(error.localizedDescription)")
        }
    }
    
    
    
    
    func configureCell(cell: ItemViewCell, indexPath: NSIndexPath) {
        let item=fetchedResultsController.objectAtIndexPath(indexPath) as! EvaluateItem
        cell.itemDesc.text=item.desc
        cell.itemRank.text="\(item.rank!)"
        cell.itemRankSlider.value=(item.rank?.floatValue)!
        cell.itemRemark.text=item.remark
    }


}

extension ItemViewController:UITableViewDataSource{
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
            
            let cell = tableView.dequeueReusableCellWithIdentifier("itemCell", forIndexPath: indexPath)
                    as! ItemViewCell
            
            configureCell(cell, indexPath: indexPath)
            
            return cell
    }

}