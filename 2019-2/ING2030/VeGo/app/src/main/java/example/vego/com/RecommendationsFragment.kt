package example.vego.com


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ListView
import android.widget.Toast
import kotlinx.android.synthetic.*

/**
 * A simple [Fragment] subclass.
 */
class RecommendationsFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view: View = inflater.inflate(R.layout.fragment_recommendations, container, false)



        var recom_list = view.findViewById<ListView>(R.id.recom_list)
        var list = mutableListOf<Recommendation>()

        list.add(Recommendation("Lentejas", "Alto en proteínas y hierro", R.drawable.lentejas))
        list.add(Recommendation("Porotos con zapallo", "Alto en proteínas y hierro", R.drawable.porotos))
        list.add(Recommendation("Lasagna de berenjenas", "Alto en hierro", R.drawable.lasagna_berenjenas))
        list.add(Recommendation("Merluza al vapor", "Alto en proteínas y vitamina B12", R.drawable.merluza_al_vapor))
        list.add(Recommendation("Ensalada de Quínoa", "Alto en hierro", R.drawable.quinoa))

        recom_list.adapter = RecomAdapter(activity!!.applicationContext, R.layout.row, list)

        recom_list.setOnItemClickListener { parent: AdapterView<*>, view:View, position:Int, id:Long ->
            Toast.makeText( activity!!.applicationContext, "Receta aún no disponible", Toast.LENGTH_LONG).show()


        }


        return view
    }


}
