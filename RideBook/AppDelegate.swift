//
//  AppDelegate.swift
//  RideBook
//
//  Created by hupei on 16/5/17.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit
import CoreData

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?
    lazy var coreDataStack=CoreDataStack()

    func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
        
        let tabBarController=window!.rootViewController as! UITabBarController
        
        let itemViewController=tabBarController.viewControllers![1] as! ItemViewController
        itemViewController.coreDataStack=self.coreDataStack
        let personViewController=tabBarController.viewControllers![2] as! PersonViewController
        personViewController.coreDataStack=self.coreDataStack
        let vehicleViewController=tabBarController.viewControllers![3] as! VehicleViewController
        vehicleViewController.coreDataStack=self.coreDataStack
        
        
        let jdm=JsonDataManager()
        jdm.importJSONSeedDataIfNeeded(coreDataStack)
        
        return true
    }

    func applicationDidEnterBackground(application: UIApplication) {
        coreDataStack.saveContext()
    }

    func applicationWillTerminate(application: UIApplication) {
        coreDataStack.saveContext()
    }

}

