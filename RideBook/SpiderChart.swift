//
//  SpiderChart.swift
//  RideBook
//
//  Created by hupei on 16/6/2.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit
@IBDesignable
class SpiderChart: UIView {

    var chartDataSeries:[[Float]]!=[[5.8,6.3,6.5,6.2,7.5,6.9],[5.4,6.8,6.7,6.3,7.1,6.7]]{
        didSet{
            //setup chart range
            var maxs=[Float]()
            var mins=[Float]()
            
            for i in chartDataSeries{
                maxs.append(i.maxElement()!)
                mins.append(i.minElement()!)
            }
            maxValue=Float(lroundf(maxs.maxElement()!+Float(subUnit)))
            minValue=Float(Int(mins.minElement()!-Float(2*subUnit)))
            seriesCount=chartDataSeries.count
        }
    }
    
    var chartHeadTitle:[NSString]=["动力性","稳定性","舒适性","操控性","静音性","便利性"]
    var chartSeiersTitle:[NSString]=["1号车","2号车"]
    
    let colorSeries=[UIColor.redColor(),UIColor.greenColor(),UIColor.blueColor(),UIColor.brownColor()]
    
    var minValue:Float=3.0{
        didSet{
            setNeedsDisplay()
        }
    }
    var maxValue:Float=8.0{
        didSet{
            setNeedsDisplay()
        }
    }
    var scale:CGFloat{
        return chartRadius/CGFloat(maxValue-minValue)
    }
    
    var subUnit:Float=1.0{
        didSet{
            setNeedsDisplay()
        }
    }
    
    var axisWidth:CGFloat=3{
        didSet{
            setNeedsDisplay()
        }
    }
    
    var seriesCount:Int=6
    
    var chartCenter:CGPoint{
        return convertPoint(center, fromView: self.superview)
    }
    
    var chartRadius:CGFloat{
        return min(bounds.height,bounds.width)*0.4
    }
    
    var chartStartAngle:Float=90.0
    
    func seriesPoint(index:Int,value:Float)->CGPoint{
        let angle=Float(M_PI)/180.0*(chartStartAngle+Float(index)*360.0/Float(seriesCount))
        let point=CGPointMake(chartCenter.x+scale*valueTrans(value)*CGFloat(cos(angle)),chartCenter.y-scale*valueTrans(value)*CGFloat(sin(angle)))
        return point
    }
    
    func valueTrans(value:Float)->CGFloat{
        return CGFloat(value)-CGFloat(minValue)
    }
    
    
    func drawAxis(){
        let bezierPath=UIBezierPath()
        for i in 0...seriesCount-1{
            bezierPath.moveToPoint(chartCenter)
            bezierPath.addLineToPoint(seriesPoint(i, value: maxValue))
            UIColor.blackColor().setStroke()
            bezierPath.lineWidth=axisWidth
            bezierPath.stroke()
        }
    }
    func drawGrid(){
        var value=minValue
        while value<maxValue{
            value=value+subUnit
            var data=[Float]()
            for _ in 0...seriesCount-1{
                data.append(value)
            }
            drawASeries(data, color: UIColor.grayColor(), width: axisWidth/3)
        }
        
        
    }
    
    func drawASeries(data:[Float],color:UIColor,width:CGFloat){
        let bezierPath=UIBezierPath()
        var points=[CGPoint]()
        for j in 0...data.count-1{
            points.append(seriesPoint(j, value: data[j]))
        }
        bezierPath.moveToPoint(points[0])
        for j in 1...points.count-1{
            bezierPath.addLineToPoint(points[j])
        }
        bezierPath.closePath()
        color.setStroke()
        bezierPath.lineWidth=width
        bezierPath.stroke()
    }
    
    func drawData(){
        for i in 0...chartDataSeries.count-1{
            let index = i % colorSeries.count
            drawASeries(chartDataSeries[i],color: colorSeries[index],width: 2)
        }
    }
    
    func drawText(){
        var value=minValue
        while value<maxValue{
            value=value+subUnit
            let unitStr=NSString(format: "%.1f", value)
            let point=seriesPoint(0, value: value)
            let offsetPoint=CGPointMake(point.x+axisWidth, point.y-axisWidth)
            unitStr.drawAtPoint(offsetPoint, withAttributes: nil)
            }
        for i in 0...seriesCount-1{
            let label=chartHeadTitle[i]
            let point=seriesPoint(i, value: maxValue*1.05)
            let offsetPoint=CGPointMake(point.x-2.0*axisWidth, point.y-2.0*axisWidth)
            label.drawAtPoint(offsetPoint, withAttributes: nil)
        }
        
        
    }
    
    override func drawRect(rect: CGRect) {
        
        drawGrid()
        drawAxis()
        drawData()
        drawText()
    }
}
