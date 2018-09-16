//
//  TableView.swift
//  PillUp
//
//  Created by Shayan on 9/16/18.
//  Copyright © 2018 Shayan. All rights reserved.
//

import Foundation
import UIKit

class CTableViewCell: UITableViewCell {
    
    var iconView: UIImageView!
    var title: UILabel!
    var desc: UILabel!
    var time: UILabel!
    var button: UIButton!
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        
        iconView = UIImageView()
        title = UILabel()
        desc = UILabel()
        time = UILabel()
        button = UIButton()
        
        self.addSubview(iconView)
        self.addSubview(title)
        self.addSubview(desc)
        self.addSubview(time)
        self.addSubview(button)
        
        iconView.snp.makeConstraints { make in
            make.left.top.bottom.equalTo(25)
            make.centerY.equalToSuperview()
            make.height.width.equalTo(33)
        }
        
        title.snp.makeConstraints { make in
            make.left.equalTo(iconView.snp.right).offset(13)
            make.top.equalToSuperview().offset(20)
        }
        
        desc.snp.makeConstraints { make in
            make.left.equalTo(title.snp.left)
            make.top.equalTo(title.snp.bottom).inset(5)
        }
        
        time.snp.makeConstraints { make in
            make.right.equalToSuperview().offset(25)
            make.centerY.equalTo(title)
        }
        
        button.snp.makeConstraints { make in
            make.right.equalTo(time.snp.right)
            make.centerY.equalTo(desc.snp.centerY)
        }
        
        iconView.image = #imageLiteral(resourceName: "Bitmap")
        title.font = UIFont.systemFont(ofSize: 20, weight: .medium)
        desc.font = UIFont.systemFont(ofSize: 12, weight: .medium)
        time.font = UIFont.systemFont(ofSize: 13, weight: .thin)
        
        title.text = "Advil"
        desc.text = "Before your meal"
        time.text = "12:30PM"
        
        
    }
    
    func setup() {
        
    }
    
    override init(style: UITableViewCellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
    }
    
    
    
    
}
