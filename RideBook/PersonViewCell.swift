//
//  PersonViewCell.swift
//  RideBook
//
//  Created by hupei on 16/5/30.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit

class PersonViewCell: UITableViewCell {

    var person:Person!{
        didSet{
            updateUI()
        }
    }
    
    private func updateUI(){
        nameLabel?.text=person.name!
        positionLabel?.text=person.position!
    }
    
    @IBOutlet weak var attendSwitch: UISwitch!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var positionLabel: UILabel!
    @IBAction func attendCheck(sender: AnyObject) {
        
    
    }
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
