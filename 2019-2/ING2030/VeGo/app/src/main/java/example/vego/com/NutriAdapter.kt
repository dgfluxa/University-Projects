package example.vego.com

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.ImageView
import android.widget.ProgressBar
import android.widget.TextView

class NutriAdapter(var mCtx: Context, var resources:Int, var items:List<Nutrition>):
    ArrayAdapter<Nutrition>(mCtx, resources, items) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val layoutInflater: LayoutInflater = LayoutInflater.from(mCtx)
        val view: View = layoutInflater.inflate(resources, null)

        val imageView:ImageView = view.findViewById(R.id.arrow)
        val titleTextView: TextView = view.findViewById(R.id.textView)
        val percentageTextView: TextView = view.findViewById(R.id.textView2)
        val progressBar: ProgressBar = view.findViewById(R.id.progressBar)

        var mItem:Nutrition = items[position]

        imageView.setImageDrawable(mCtx.resources.getDrawable(mItem.img))
        titleTextView.text = mItem.title
        percentageTextView.text = (mItem.percentage + "%")
        progressBar.progress = mItem.percentage.toInt()



        return view
    }

}